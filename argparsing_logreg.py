import argparse, textwrap

def my_logistic_regression( penalty , fit_intercept , max_iter , tol ) :
    from sklearn.linear_model import LogisticRegression

    # define a logistic regression object with your input params
    clf = LogisticRegression ( penalty = penalty , fit_intercept =
    fit_intercept , max_iter = max_iter , tol = tol )

    return clf

# Add description and epilog
parser = argparse.ArgumentParser(prog='my_logistic_regression',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                      A helper function for LogisticRegression
                                     ------------------------------------------------------------
                                      This function calls LogisticRegression from sklearn 
                                      with the following four parameters: 
                                      --penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'
                                                'l1': Use a L1 penalty term;
                                                'l2': Use a L2 penalty term which is the default choice;
                                                'elasticnet': Use both L1 and L2 penalty terms;
                                                None: No penalty is used.
                                      --fit_intercept: bool, default=True
                                      --max_iter: int, default=100
                                      --tol: float, default=1e-4
                                     
                                    '''),
        epilog=textwrap.dedent('''\
                                     ------------------------------------------------------------
                                      For more information visit:
                                      https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
                                     ''')
                    )

# Add the four arguments
parser.add_argument("--penalty", type=str, choices=['l1', 'l2', 'elasticnet', None], default="l2", 
                    help="Specify the norm of the penalty.")
parser.add_argument("--fit_intercept", action="store_true", 
                    help="Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.")
parser.add_argument("--max_iter", type=int, default=100,
                    help="Maximum number of iterations taken for the solvers to converge.")
parser.add_argument("--tol", type=float, default=10**-4,
                    help="Tolerance for stopping criteria.")

args = parser.parse_args()
print(args)

