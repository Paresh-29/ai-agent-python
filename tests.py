from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    working_dir = "calculator"
    # tests for getting files info
    # root_contents = get_files_info(working_dir)
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "../")
    # print(pkg_contents)

    # test for getting file content
    # print(get_file_content(working_dir, "lorem.txt"))
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "pkg/notexists.py"))
    # print(get_file_content(working_dir, "/bin/cat"))

    # tests for writing in file
    # print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file(working_dir, "pkg2/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file(working_dir, "/tmp/temp.txt", "this should not be allowed"))

    #  (should print the calculator's usage instructions)
    print(run_python_file(working_dir, "main.py"))
    # (should run the calculator... which gives a kinda nasty rendered result)
    print(run_python_file(working_dir, "main.py", ["3 + 5"]))

    print(run_python_file(working_dir, "tests.py"))

    #  (this should return an error)
    print(run_python_file(working_dir, "../main.py"))

    # (this should return an error)
    print(run_python_file(working_dir, "nonexistent.py"))


main()
