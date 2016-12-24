def modButtonPush(old, new, primary_modkeystate, second_modkeystate1, second_modkeystate2):
        if old != new:
                old = new
                if new == 0: # button pushed down
                        # flip the sate of modkeystate
                        primary_modkeystate = abs(primary_modkeystate - 1)
                        if primary_modkeystate == 1: # if you're turning a key on
                                # turn off the other two
                                second_modkeystate1 = 0
                                second_modkeystate2 = 0
                                
                                
        return old, new, primary_modkeystate, second_modkeystate1, second_modkeystate2

print(modButtonPush(1, 0, 1, 0, 0))
