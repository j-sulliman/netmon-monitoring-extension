def get_host_response_time(host):
    
    import subprocess
    
    receiveOutput = subprocess.Popen("ping -c 1 {}".format(host), shell=True, stdout=subprocess.PIPE).stdout
    output = receiveOutput.read()
    print(output)
    output = output.decode()
    output = output.split("time=")
    output = output[1].split(" ms")
    output = output[0].split(".")

    return output[0]
