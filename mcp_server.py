import sys, json
from client import WebFormInputSchemaAutoMapper

def main():
    mapper = WebFormInputSchemaAutoMapper()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            method = req.get("method")
            rid = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "map_form_fields", "description": "Map form inputs to schema.", "inputSchema": {"type": "object", "properties": {"form_inputs": {"type": "array"}}, "required": ["form_inputs"]}},
                        {"name": "run_benchmark_form_mapper", "description": "Run self-test.", "inputSchema": {"type": "object"}}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "map_form_fields":
                    out = mapper.map_form_fields(args.get("form_inputs", []))
                elif tname == "run_benchmark_form_mapper":
                    out = mapper.run_benchmark_form_mapper()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
