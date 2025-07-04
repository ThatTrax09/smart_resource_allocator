import re

class ChatAssistant:
    def __init__(self, task_assigner):
        self.assigner = task_assigner
        self.assignments = task_assigner.get_assignments()
        self.workers = task_assigner.get_workers()
        self.machines = task_assigner.get_machines()

    def handle_query(self, query):
        query = query.lower().strip()

        match_task = re.match(r"who is doing (\w+)\??", query)
        if match_task:
            skill = match_task.group(1)
            return self._who_is_doing(skill)

        match_person = re.match(r"what is (\w+) assigned to\??", query)
        if match_person:
            name = match_person.group(1).capitalize()
            return self._what_is_assigned_to(name)
        
        match_count_tasks = re.match(r"how many (\w+) are doing (\w+)\??", query)
        if match_count_tasks:
            type = match_count_tasks.group(1)
            skill = match_count_tasks.group(2)
            return self._how_many_doing(type, skill)

        if "list all workers" in query:
            return self._list_all_workers()
        
        if "list all machines" in query:
            return self._list_all_machines()

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
    
    def _how_many_doing(self, type, skill):
        count = 0
        list_assigned = []
        if type == 'machines':
            list_assigned = self.machines
        else:
            list_assigned = self.workers
        if len(list_assigned) != 0:
            for worker in list_assigned:
                for assignment in self.assignments[worker]:
                    if assignment['required_skill'] == skill:
                        count += 1
                        break
        return count
    def _list_all_workers(self):
        print('The workers are:')
        return(', '.join(self.workers))
    
    def _list_all_machines(self):
        print('The machines are:')
        return(', '.join(self.machines))