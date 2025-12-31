import argparse
from weekly import Weekly


def main():
    parser = argparse.ArgumentParser(description="Weekly topic tracker")

    sub = parser.add_subparsers(dest="cmd", required=True)

    # show
    sub.add_parser("show")

    # skip topic
    sub.add_parser("skip")

    # topic done
    sub.add_parser("done")

    # reset score
    sub.add_parser("reset-score")

    # reset streak
    sub.add_parser("reset-streak")

    # reset everything
    sub.add_parser("reset")

    # list topics
    sub.add_parser("list")

    # add topics
    add = sub.add_parser("add")
    add.add_argument("topics", help="Colon-separated topics")

    args = parser.parse_args()

    w = Weekly()

    if args.cmd == "show":
        w.show()

    elif args.cmd == "done":
        w.topic_done()

    elif args.cmd == "reset-score":
        w.reset_score()

    elif args.cmd == "reset-streak":
        w.reset_streak()

    elif args.cmd == "reset":
        w.reset_all()

    elif args.cmd == "skip":
        w.skip_topic()

    elif args.cmd == "list":
        w.list_topics()

    elif args.cmd == "add":
        w.add_topics(args.topics)

if __name__ == "__main__":
    main()
