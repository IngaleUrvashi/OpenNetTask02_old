REST API: 
The task is completed for below URL : https://github.com/thundercomb/poetrydb/blob/master/README.md
The Test Cases covered are as follows: 

![Screenshot 2024-04-01 214840](https://github.com/IngaleUrvashi/OpenNetTask02/assets/165666146/8e7a3937-c1ae-400b-9cdc-16dfcf91d065)

While writing the test cases both Positive and Negative scenarios are covered

Steps to run test cases:
1) Clone the Repository
2) Open the project in any Python IDE
3) Run the given command in a console: **python -m pytest -v**

The result will be as follows: 
=============================================== test session starts ===============================================
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0 -- C:\Users\URVASHI INGALE\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\URVASHI INGALE\Desktop\OpenNet-Task02
collected 10 items

test_author_api.py::test_can_call_endpint PASSED                                                             [ 10%]
test_author_api.py::test_author_exist[Ernest Dowson] PASSED                                                  [ 20%]
test_author_api.py::test_author_exist[Emily Dickinson] PASSED                                                [ 30%]
test_author_api.py::test_author_exist[This Test Case Should Fail] FAILED                                     [ 40%]
test_author_api.py::test_title_author_linecount PASSED                                                       [ 50%]
test_author_api.py::test_lines_exist[Latitudeless Place.] PASSED                                             [ 60%]
test_author_api.py::test_lines_exist[This Test Case Should Fail] FAILED                                      [ 70%]
test_author_api.py::test_linecount[3] PASSED                                                                 [ 80%]
test_author_api.py::test_linecount[5] PASSED                                                                 [ 90%]
test_author_api.py::test_linecount[0] FAILED  


   
