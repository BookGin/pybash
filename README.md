# Pybash
Run shell scripts and Linux commands in python. Usage of redirection, pipe are identical to bash.

## Usage
#### Run commands synchronously
```python
$ python -q
>>> import pybash
>>> files = pybash.run('find ./example-dir')
>>> print(files)
./example-dir
./example-dir/example2.png
./example-dir/example3.mp3
./example-dir/example1.doc
```
#### You can still use redirection, pipe, &&, ||
```python
>>> pybash.run('hexdump -C ./README.md | tr "[:lower:]" "[:upper:]" > hex.out')
```
#### Run commands asynchronously
```python
>>> job = pybash.run('sleep 10 && echo "wakeup!"', asynchronous = True)
>>> job.isFinished()
False
>>> job.wait()
# after 10 seconds
'wakeup!'
>>> job.isFinished()
True
```
#### Get return code
```python
>>> pybash.run('echo hello', get_return_code = True)
0
```