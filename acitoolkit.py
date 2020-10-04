import paramiko
from config.environment import *


ssh = paramiko.SSHClient()


def run_command_on_device(ip_address, username, password, command):
    """ Connect to a device, run a command, and return the output."""

    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    total_attempts = 3
    for attempt in range(total_attempts):
        try:
            # Connect to router using username/password authentication.
            ssh.connect(ip_address,
                        username=username,
                        password=password,
                        look_for_keys=False)

            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            # Read output from command.
            command_output = ssh_stdout.readlines()
            # Close connection.
            ssh.close()
            return (command_output)
        except Exception as error_message:
            print("Unable to connect")
            print(error_message)


def print_output(output):
    # Make sure we didn't receive empty output.
    if output != None:
        for line in output:
            print(line)

if __name__ == '__main__':
    menu = {}
    menu['1 -'] = "Ports with particular VLAN."
    menu['2 -'] = "Ports connected to server."
    menu['3 -'] = "EPGs in port."
    menu['4 -'] = "VLANs per server."
    menu['5 -'] = "Fabric ports status per server."
    menu['6 -'] = "Server commissioning."
    menu['7 -'] = "Server decommissioning."
    menu['8 -'] = "New tenant."
    menu['99 -'] = "Exit."
    while True:
      print("****** ACI TOOLKIT ******:")
      options=menu.keys()
      #options.sort()

      for entry in options:
        print (entry, menu[entry])


      selection=input("Please Select:")

      if selection =='1':
          encapVLAN = input ("Encapsulation VLAN: ")
          command = "moquery -c fvRsPathAtt -f 'fv.RsPathAtt.encap == \"vlan-" + encapVLAN + "\"' -o table"
          print_output(run_command_on_device(apic1_ip, apic_username, apic_password, command))
      elif selection == '2':
          server_name = input("Server name: ")
          command = "moquery -c infraHPortS | grep dn | grep  "+ server_name
          print_output(run_command_on_device(apic1_ip, apic_username, apic_password, command))
      elif selection == '3':
          print ("find")
      elif selection == '6':
          break
      else:
          print ("Unknown Option Selected!")