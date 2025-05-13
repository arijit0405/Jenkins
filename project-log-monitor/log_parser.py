def count_errors_in_log(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if 'error' in line.lower():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return -1


if __name__ == "__main__":
    log_file = "demo.log"  # Make sure this file exists in the same directory
    error_count = count_errors_in_log(log_file)
    if error_count != -1:
        print(f"Total 'error' lines found: {error_count}")
