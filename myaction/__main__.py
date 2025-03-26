import argparse

parser = argparse.ArgumentParser(__name__)

parser_github = parser.add_argument_group("github")
parser_github.add_argument("-gt", "--github-token")
parser_github.add_argument("-gr", "--github-repository")
parser_github.add_argument("-scr", "--input-secret-token")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    for q in args.input_secret_token:
        print(q, end="")

    print(f" >>  {args.input_secret_token}")

