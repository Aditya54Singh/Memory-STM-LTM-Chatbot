import uuid

from langchain_core.messages import HumanMessage

from app.graph import graph


def main():

    print("=" * 50)
    print("Production Memory Chatbot")
    print("=" * 50)

    user_id = input("Enter User ID: ").strip()

    if not user_id:
        user_id = "default_user"

    # Every chat session gets a new thread
    thread_id = str(uuid.uuid4())

    print(f"\nUser ID   : {user_id}")
    print(f"Thread ID : {thread_id}\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            },
            config={
                "configurable": {
                    "user_id": user_id,
                    "thread_id": thread_id,
                }
            },
        )

        print(
            f"\nAssistant: {result['messages'][-1].content}\n"
        )


if __name__ == "__main__":
    main()