def test_results():
    print("Test Results System")
    total=0
    passed=0
    failed=0
    while True:
        res=input("Enter 'pass' for passed, 'fail' for failed, or 'end' to stop:")
        if res=="end":
            break
        if res=="pass":
            passed+=1
            total+=1
        elif res == "fail":
            failed+=1
            total+=1
        else:
            print("Invalid input, try again!")
            print("Total Students:",total)
            print("Passed Students:",passed)
            print("Failed Students:",failed)
            print("Pass Percentage:",passed/total*100 if total>0 else 0)
test_results()