import argparse
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

def main():
    parser = argparse.ArgumentParser(description='Initiate a chat with the assistant to process a given message.')
    parser.add_argument('message', help='The message to process.')
    args = parser.parse_args()

    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
    user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

    user_proxy.initiate_chat(assistant, message=args.message)

if __name__ == "__main__":
    main()
