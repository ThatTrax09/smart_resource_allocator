import json
from collections import defaultdict

class TaskAssigner:
    def __init__(self, resources_file, tasks_file):
        self.resources_file = resources_file
        self.tasks_file = tasks_file
        self.resources = []
        self.tasks = []
        self.assignments = defaultdict(list)  # {resource_name: [task1, task2]}
        self.load_data()

    def load_data(self):
        with open(self.resources_file, 'r') as rf:
            self.resources = json.load(rf)['resources']

        with open(self.tasks_file, 'r') as tf:
            self.tasks = json.load(tf)['tasks']

        # Add a 'current_load' field to each resource to track how many tasks they have
        for r in self.resources:
            r['current_load'] = 0

    def is_available(self, resource):
        return resource['current_load'] < resource['max_tasks']

    def has_skill(self, resource, skill):
        return skill in resource['skills']

    def assign_tasks(self):
        for task in self.tasks:
            assigned = False
            # Sort by least loaded to ensure fairness
            sorted_resources = sorted(self.resources, key=lambda r: r['current_load'])
            for resource in sorted_resources:
                if self.is_available(resource) and self.has_skill(resource, task['required_skill']):
                    self.assignments[resource['name']].append(task)
                    resource['current_load'] += 1
                    assigned = True
                    break
            if not assigned:
                print(f"⚠️  Could not assign task '{task['name']}' (skill: {task['required_skill']})")

    def get_assignments(self):
        return self.assignments

    def print_assignments(self):
        print("=== Task Assignments ===")
        for resource, tasks in self.assignments.items():
            print(f"{resource} is assigned:")
            for task in tasks:
                print(f"  - {task['name']} (Skill: {task['required_skill']})")
        print("========================")

# Example usage
if __name__ == "__main__":
    assigner = TaskAssigner(
        resources_file="smart_resource_allocator/data/resources.json",
        tasks_file="smart_resource_allocator/data/tasks.json"
    )
    assigner.assign_tasks()
    assigner.print_assignments()
