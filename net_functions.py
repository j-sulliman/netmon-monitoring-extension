def get_host_response_time(host):
    
    import subprocess
    import datetime
    
    try:
        receiveOutput = subprocess.Popen("ping -c 1 {}".format(host), shell=True, stdout=subprocess.PIPE).stdout
        output = receiveOutput.read()
        output = output.decode()
        output = output.split("time=")
        output = output[1].split(" ms")
        output = output[0].split(".")
        output = output[0]
    except IndexError:
        f = open("netmon.log", "a")
        f.write("{} - Unable to ping host {}.  Is address correct\n".format(datetime.datetime.now(), host))
        output = receiveOutput.read()
        output = output.decode()
        f.close()
    return output
