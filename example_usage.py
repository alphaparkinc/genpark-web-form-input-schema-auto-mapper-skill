from client import WebFormInputSchemaAutoMapper
import json

def main():
    mapper = WebFormInputSchemaAutoMapper()
    res = mapper.run_benchmark_form_mapper()
    print("Form Auto-Mapper Benchmark Result:")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
