import click
import os
from tqdm import tqdm

@click.command()
@click.option("--host", type=str)
def main(host):
    print(f"CALC MTU to {host}", flush=True)
    l = 0
    r = 127992 + 1
    max_cnt = 17
    cnt = 0
    prc = 0
    for i in tqdm(range(17)):
        if l + 1 >= r:
            break
        cnt += 1
        m = (l + r) // 2
        if os.system(f"ping -M do -s {m} {host} -c 1 1> logs.txt 2> errlogs.txt") == 0:
            l = m
        else:
            r = m
        #print(f"{int(100 * cnt/max_cnt)}% done")
    if l == 0:
        print("MTU = 0, maybe host is wrong")
    else:
        print(f"MTU = {l}({l+28})")


if __name__ == "__main__":
    main(auto_envvar_prefix="CALC_MTU")

