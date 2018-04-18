import gym
import sys

args = sys.argv
largs = len(args)
# print(args)
def largs_is(rng): return (largs in rng)
envids = [spec.id for spec in gym.envs.registry.all() ]        


if largs == 1:
    print("usage: `python3 openai_demo [command] \{*args\}")

elif largs_is([2]) and args[1] == "help":
    print("./openai_demo")
    print("              help")
    print("              list \{filter\}")
    print("              run  [environment name] \{verbose?\}")

elif largs_is([2,3]) and args[1] == "list":
    
    # with filter
    if largs_is([3]):
        new_envids = []
        ftr = args[2].lower()
        for eid in envids:
            tmp_eid = eid.lower()
            if ftr in tmp_eid and tmp_eid.index(ftr) == 0: new_envids.append(eid)
        envids = new_envids
    
    for envid in envids:
        print(envid)

elif largs_is([3,4]) and args[1] == "run":

    envid = args[2]
    verbose = largs_is([4]) and args[3] == "True"
    print(envid)
    if not (envid in envids):
        print("[!] Given environment id not found.")
        print("    Use `list` to list environment options.")
        quit()
    else:
        steps       = 200
        env         = gym.make(envid)
        observation = env.reset()

        log = lambda x, y: None
        if verbose: log = lambda x, y: print("observation:",x,"\naction:",y)

        for t in range(steps):
            # render
            env.render()
            # random action
            action = env.action_space.sample()
            # update
            observation, reward, done, info = env.step(action)
            # log
            log(observation, action)
            if done: break

else:

    print("[?] use `help` to get some help.")