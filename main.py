from class_qlearning  import q_learning

if __name__=='__main__':
    path = 'DataTugasML3.txt'
    ql = q_learning(path)
    ql.run()

    print(ql.Q)