#!/usr/bin/python3

# Remove duplicate lines from the text file.
def remove_duplicates(file_path):
	try:
		with open(file_path, 'r') as file:
			lines = file.readlines()
		
		# Remove duplicates by converting lines to a set and then back to a list
		unique_lines = list(set(lines))

		# Write the unique lines back to the file
		with open(file_path, 'w') as file:
			file.writelines(unique_lines)

		print(f"Duplicate lines removed from '{file_path}'")

	except Exception as e:
		print(f"An error occurred: {e}")


# Sort the lines of the text file in ascending or descending order.
def sort_file(file_path, ascending=True):
	try:
		with open(file_path, 'r') as file:
			lines = file.readlines()

		# Sort the lines based on the `ascending` flag
		sorted_lines = sorted(lines, reverse=not ascending)

		# Write the sorted lines back to the file
		with open(file_path, 'w') as file:
			file.writelines(sorted_lines)

		order = "ascending" if ascending else "descending"
		print(f"Input file '{file_path}' sorted in {order} order.")

	except Exception as e:
		print(f"An error occurred: {e}")


# Write the zone file
def write_zone_file(input, rpz):
	try:
		with open(rpz, "w") as rpz_file:
			rpz_file.write("""; BIND RPZ Zone File
;
$TTL    86400
@       IN      SOA     localhost. root.localhost. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                          86400 )       ; Negative Cache TTL
;
@       IN      NS      localhost.
""")
			with open(input) as input_file:
				for line in input_file:
					line = line.rstrip()
					rpz_file.write(f"{line} CNAME .\n")
					rpz_file.write(f"*.{line} CNAME .\n")

		print(f"RPZ zone file '{rpz}' has been generated.")

	except Exception as e:
		print(f"An error occurred: {e}")


# Set the input file and RPZ file names to string
input_file = "input.txt"
rpz_file = "db.blacklist"

# Process the input to RPZ output
remove_duplicates(input_file)
sort_file(input_file)
write_zone_file(input_file, rpz_file)
