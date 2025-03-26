import argparse

parser = argparse.ArgumentParser(__name__)

parser_github = parser.add_argument_group("github")
parser_github.add_argument("-gt", "--github-token")
parser_github.add_argument("-gr", "--github-repository")
parser_github.add_argument("-scr", "--input-custom-param")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    for q in args.input_custom_param:
        print(q)

    print(f" >>  {args.input_custom_param}")

