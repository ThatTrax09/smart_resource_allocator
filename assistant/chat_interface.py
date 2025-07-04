import re

class ChatAssistant:
    def __init__(self, task_assigner):
        self.assigner = task_assigner
        self.assignments = task_assigner.get_assignments()

    def handle_query(self, query):
        query = query.lower().strip()

        # 1. Who is doing <task_type>?
        match_task = re.match(r"who is doing (\w+)\??", query)
        if match_task:
            skill = match_task.group(1)
            return self._who_is_doing(skill)

        # 2. What is <name> assigned to?
        match_person = re.match(r"what is (\w+) assigned to\??", query)
        if match_person:
            name = match_person.group(1).capitalize()
            return self._what_is_assigned_to(name)

        # 3. List all task assignments
        if "list all task assignments" in query:
            return self._list_all_assignments()

        return "Sorry, I didn't understand that question."

    def _who_is_doing(self, skill):
        result = []
        for resource, tasks in self.assignments.items():
            for task in tasks:
                if task["required_skill"] == skill:
                    result.append(resource)
                    break
        if result:
            return f"{', '.join(result)} are doing {skill} tasks."
        else:
            return f"No one is currently assigned to {skill} tasks."

    def _what_is_assigned_to(self, name):
        tasks = self.assignments.get(name)
        if not tasks:
            return f"{name} has no assigned tasks."
        task_list = [task["name"] for task in tasks]
        return f"{name} is assigned to: {', '.join(task_list)}"

    def _list_all_assignments(self):
        if not self.assignments:
            return "No assignments have been made yet."
        lines = []
        for resource, tasks in self.assignments.items():
            task_names = [t['name'] for t in tasks]
            lines.append(f"{resource}: {', '.join(task_names)}")
        return "\n".join(lines)
