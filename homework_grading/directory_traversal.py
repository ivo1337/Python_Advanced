import os


def generate_report(directory):
    # Get all files in the given directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Group files by extension
    files_by_extension = {}
    for file in files:
        extension = os.path.splitext(file)[1][1:]  # Extract extension without the dot
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)

    # Sort extensions alphabetically
    sorted_extensions = sorted(files_by_extension.keys())

    # Write file information in report.txt
    with open(os.path.join(directory, 'report.txt'), 'w') as report_file:
        for extension in sorted_extensions:
            report_file.write(f'.{extension}\n')
            files = sorted(files_by_extension[extension])
            for file in files:
                report_file.write(f'--- {file}\n')


# User usage
directory_path = input()
generate_report(directory_path)
