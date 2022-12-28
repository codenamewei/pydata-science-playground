### Terms in Asyncio

- Coroutine
  - computer program components that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed. 
  - non-preemptive multitask: an early version of multitasking that allocates the CPU to a process until the process makes its system call.
  - At the heart of asyncio are coroutines. Coroutines are declared with the async and await syntax. They are in essence awaitable functions.
  - coroutines can execute non-blocking I/O asynchronously
  - You can run an asyncio coroutine via the run() function, by awaiting it within another coroutine, or by scheduling it as Task.
- Subprocess
  - <TBD>
- Task 
  - An asyncio Task is an object that schedules and independently runs an asyncio coroutine.

### Other terms in Asyncio
- await 
  - Just a term more formal that wait


### asyncio_wait.py

<img src="https://user-images.githubusercontent.com/33477318/185338417-9feab028-b726-49c3-ad40-c7e887dbf34e.png" width="500">
