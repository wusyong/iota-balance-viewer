# Imports the PyOTA library
from iota import Iota
import config

index = int(input("What index would you like to start to search? "))
numberOfAddresses = int(input("How many addresses would you like to check for balance? "))
node = config.node
seed = config.seed

# Generates addresses of a given seed using the "get_new_addresses()" function
def addressGenerator():
	# Although generating addresses won't connect to the node
	api = Iota(node, seed)
	gna_result = api.get_new_addresses(index=index, count=numberOfAddresses)
	addresses = gna_result['addresses']
	i = 0
	sum = 0
	while i < numberOfAddresses:
		address = [addresses[i]]
		balance = addressBalance(address)
		print ("Index " + str(index + i) + " address " + str(address[0]) + " has balance: " + str(balance))
		sum += balance
		i += 1
	print ("Above addresses have total balance of " + str(sum) + " iota!")

# Sends a request to the IOTA node and gets the current confirmed balance
def addressBalance(address):
	api = Iota(node)
	gb_result = api.get_balances(address)
	balance = gb_result['balances']
	return (balance[0])

def main():
	print ("Checking balance in " + str(numberOfAddresses) + " addresses start from index " + str(index) + " for the seed!\n This may take a while...")
	addressGenerator()

if __name__ == '__main__':
    main()
