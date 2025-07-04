# Smart resource allocator

The repository has been setup according to the instructions provided in the task. Each module is available in its respective folder in the given structure.

```
smart_resource_allocator
├───assistant
│   └─── chat_interface.py
├───data
│    └─── resources.json
│    └─── tasks.json
└───logic
│    └─── task_assigner.py
└───main.py
└───README.md
```
To run the code for this application, you can clone this repository locally and just execute the main file alone in the command line:

``` 
python main.py 
```
The chatbot interface will be displayed in the CLI as below:

```
=== Chat Assistant Ready ===

Ask me anything (or type 'exit'):
```
The following questions can be asked to the chatbot:

- Who is doing packing/transporting/labelling?
- What is *worker name/machine name* assigned to?
- How many workers/machines are doing packing/transporting/labelling?
- list all workers
- list all machines
- list all task assignments
- To exit, just type "exit"

