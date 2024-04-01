import requests
import pytest

BASE_URL = "https://poetrydb.org/"

def test_can_call_endpint():
    response_call_endpoint = requests.get(BASE_URL)
    assert response_call_endpoint.status_code == 200

# This Test Case checks whether Author exist with given List of Inputs
@pytest.mark.parametrize("author_name", ["Ernest Dowson", "Emily Dickinson", "This Test Case Should Fail"])
def test_author_exist(author_name):
    response_author_exist = requests.get(BASE_URL +"author/" + author_name )
    data = response_author_exist.json()
    author_name_in_response = data[0]

    # This Test case is Passed when "status is 200" and "author_name" matching  the value in "author" 
    if response_author_exist.status_code == 200 and author_name_in_response['author'] == author_name:
        assert True
    # This Test case is Failed when "status is 200" response with reason Not Found
    elif response_author_exist.status_code == 200 and data['reason'] == "Not Found" :
        assert False
    # This Test Case is Failed when "status is not 200"
    else :
        assert False
    

def test_title_author_linecount():
    response_title_author_linecount = requests.get(BASE_URL + "title/Ozymandias/author,title,linecount")
    data1 = response_title_author_linecount.json()
    data_in_response = data1[0]

    #This Check whether every Value in responce matches expected values for title "Ozymandias"
    if response_title_author_linecount.status_code == 200 and data_in_response['title'] =="Ozymandias" and data_in_response['author'] == "Percy Bysshe Shelley" and data_in_response['linecount'] == "14":
       # Assert true to Pass the test case
       assert True
    else :
        #Assert false to Fail the test case
        assert False

#This Test Case check whether line provided as input exist in PoetryDB
@pytest.mark.parametrize("line_text", ["Latitudeless Place.","This Test Case Should Fail"])
def test_lines_exist(line_text):
    response_lines = requests.get(BASE_URL + "lines/" + line_text)
    data2 = (response_lines.json())[0]
    lines = data2['lines']
    line_count = int(data2['linecount'])
    for l in range (0, line_count-1):
        if (lines[l] == line_text and response_lines.status_code == 200):
            test_status = True
            print("Line is Present in appeared poem")
            break
        elif  response_lines.status_code != 200:  
            test_status = False
            
    if test_status == True:
        assert True
    elif test_status == False:
        assert False


@pytest.mark.parametrize("linecount_input", [3,0] )
def test_linecount(linecount_input):
    responce_linecount = requests.get(BASE_URL + "/linecount/" + str(linecount_input))
    list_of_poems = responce_linecount.json()
    no_of_peoms = len(list_of_poems)
    print(no_of_peoms)  

    for n in range(0, no_of_peoms-1):
        print("round is " , n )
        for result in list_of_poems:
            if int(result['linecount']) == linecount_input and len(result) == 4 and responce_linecount.status_code == 200:
                is_test_case_passed = True
            else :
                is_test_case_passed = False

    print(is_test_case_passed)
    if is_test_case_passed == True:
        assert True
    elif is_test_case_passed == False:
        assert False

            



