import termcolor as tc
import lagr
import cheb
import root

def main():
    print(tc.colored("This program performs Lagrange Interpolation with chebyshev nodes.", "cyan"))
    print(tc.colored("Enter coefficients of the polynomial (from lowest degree to highest):", "yellow"))
    coef_input = list(map(float, input().split()))
    print( "Enter domain for interpolation:" )
    domain_input = list(map(float, input().split()))
    print("Enter number of nodes (degree of polynomial):")
    num_nodes = int(input())
    try:
        degree = num_nodes - 1
        nodes = cheb.chebyshev(degree,domain_input)
        print(tc.colored("The Chebyshev nodes:", "green"))
        for node in nodes:
            print(float(node))
        result = lagr.Lagrange(nodes, coef_input, domain_input)
        print(tc.colored("The resulting Lagrange Interpolating Polynomial is:", "green"))
        print(result[0])
        print(tc.colored(f"The error bound R is: {result[1]}", "green"))
        rootx = root.roots_for(result[0], domain_input)
        if [r for r in rootx if domain_input[0] <= r <= domain_input[1]]:
            print(f"Roots of the Lagrange Interpolating Polynomial in the given domain: \n{rootx}")
        else:
            print("The roots of the Lagrange Interpolating Polynomial are outside the given domain.")
            print(f"Roots: \n{rootx}")
        L_inv = lagr.Lagrange_inv(nodes, coef_input)
        rooty = root.roots_back(L_inv)
        if rooty is not None or len(rooty) > 0:
            print(f"Roots of the Inverse Lagrange Polynomial: \n{rooty}")
        else:
            print("The Inverse Lagrange Polynomial has no roots.")
    except Exception as e:
        print(tc.colored(f"An error occurred: {e}", "red"))
    return 0
main()