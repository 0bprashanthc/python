def func1():
    print("func1")

def func2():
    print("func2")

def func3():
    print("func3")

def func4():
    print("func4")

def func5():
    print("func5")

def func6():
    print("func6")

def workflow():
    #read the txt file with workflow
    """
    1-2-3-4-5-6
    """
    wf_fobj = open("workflow.txt")
    workflow_seq = wf_fobj.readline()
    workflow = Workflow()
    workflow.execute_workflow(workflow_seq)

class Workflow(object):
    def __init__(self):
        self.workflow = None
        self.to_execute = True

    def execute_step(self,func):
        if self.to_execute:
            func()

    def execute_workflow(self,seq):
        for each_func in seq.split("-"):
            self.to_execute = True
            self.execute_step(each_func)

