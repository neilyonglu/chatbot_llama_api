from llamaapi import LlamaAPI

def llama_api(user_input):
    # Initialize the SDK
    llama = LlamaAPI("LL-v4g5J4TtrgxPYGjr3AVtA8kKaL9MXbisT8unfHxeevdcJBcuGFljeCp0wLSijcLF")
    
    # Build the API request
    api_request_json = {
        "messages": [
            {"role": "user", "content": str(user_input)},
        ],
        "functions": [
            {
                "name": "qa_machine",
                "description": "",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                },
            }
        ],
        "stream": False,
        "function_call": "get_response",
    }

    # Execute the Request
    response = llama.run(api_request_json)
    # print(json.dumps(response.json(), indent=2))
    api_output = response.json()["choices"][0]["message"]["content"]
    
    try:
        response = llama.run(api_request_json)
        response.raise_for_status()  # 抛出异常,如果状态码不是 200
        response_json = response.json()
        api_output = response_json['completion']
    except Exception as e:
        print(f"Error: {e}")
        api_output = "Sorry, please try again later."
    
    return api_output

# print(llama_api('what is llm'))