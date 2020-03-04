import subprocess as cmd


def git_push_automation():
    cp = cmd.run("git add .", check=True, shell=True)
    print("cp" , cp)
    #
    # response = input("Do you want to use the default message for this commit?([y]/n)\n")
    # message = "update the repository"
    #
    # if response.startswith('n'):
    #     message = input("What message you want?\n")

    cmd.run('git commit -m "update the repository"', check=True, shell=True)
    cmd.run("git push -u origin master -f", check=True, shell=True)


git_push_automation()
