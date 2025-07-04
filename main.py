from logic.task_assigner import TaskAssigner
from assistant.chat_interface import ChatAssistant

def main():
    assigner = TaskAssigner(
        "smart_resource_allocator/data/resources.json",
        "smart_resource_allocator/data/tasks.json"
    )
    assigner.assign_tasks()

    assistant = ChatAssistant(assigner)

    print("=== Chat Assistant Ready ===")
    while True:
        query = input("\nAsk me anything (or type 'exit'): ")
        if query.lower() == "exit":
            break
        response = assistant.handle_query(query)
        print(response)

if __name__ == "__main__":
    main()
