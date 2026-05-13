"""Thin wrapper around Outline's MCP JSON-RPC endpoint.

Reads token from env var OUTLINE_TOKEN. Usage examples in __main__.
"""
import json
import os
import sys
import time
import urllib.request

ENDPOINT = "https://dd2030-docs.kbn.one/mcp"
TOKEN = os.environ.get("OUTLINE_TOKEN")
if not TOKEN:
    sys.exit("Set OUTLINE_TOKEN env var")


def _rpc(method: str, params: dict, rpc_id: int = 1) -> dict:
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": rpc_id,
        "method": method,
        "params": params,
    }).encode()
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "dd2030-wiki-importer/0.1",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode()
    # SSE format: lines like "event: message\ndata: {json}\n"
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("data:"):
            return json.loads(line[5:].strip())
    return json.loads(raw)


def call_tool(name: str, arguments: dict) -> dict:
    """Call an MCP tool, returning the parsed JSON of the first content item."""
    result = _rpc("tools/call", {"name": name, "arguments": arguments})
    if "error" in result:
        raise RuntimeError(result["error"])
    content = result["result"]["content"]
    if not content:
        return {}
    text = content[0].get("text", "")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"_raw": text}


def call_tool_multi(name: str, arguments: dict) -> list:
    """Same as call_tool but returns all content items as parsed JSON (one per line)."""
    result = _rpc("tools/call", {"name": name, "arguments": arguments})
    if "error" in result:
        raise RuntimeError(result["error"])
    content = result["result"]["content"]
    out = []
    for c in content:
        text = c.get("text", "")
        # Multi-object responses come as multiple JSON objects separated by newlines
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                out.append({"_raw": line})
    return out


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list_collections"
    if cmd == "list_collections":
        for c in call_tool_multi("list_collections", {}):
            print(f"{c.get('id')}  {c.get('name')}")
    elif cmd == "create_collection":
        name = sys.argv[2]
        result = call_tool("create_collection", {"name": name})
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif cmd == "list_documents":
        coll_id = sys.argv[2]
        for d in call_tool_multi("list_documents", {"collectionId": coll_id}):
            print(f"{d.get('id')}  {d.get('title')}")
    elif cmd == "fetch":
        kind = sys.argv[2]  # document|collection|user
        obj_id = sys.argv[3]
        result = call_tool("fetch", {"type": kind, "id": obj_id})
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        sys.exit(f"Unknown cmd {cmd}")
