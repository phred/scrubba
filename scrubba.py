import os, re, sys, shutil

evil_comment_start = '<![if !vml]>'
evil_comment_end = '<![endif]>'
extensions_to_scrub = ['.html', '.htm']

def scrub_file(file_to_scrub, file_output):
    """ TODO: test with multiple navigation elements on page """
    page = "\n".join([line for line in file_to_scrub.readlines()])

    last_index = 0
    for match in re.finditer(r'<map', page):
        start = page.rindex(evil_comment_start, 0, match.start())
        end = page.index(evil_comment_end, match.end())

        file_output.write("<!-- begin scrub -->")
        file_output.write(page[last_index:start])
        file_output.write(page[start+len(evil_comment_start):end])
        file_output.write("<!-- end scrub -->")
        last_index = end + len(evil_comment_end)

    file_output.write(page[last_index:])


def scrub_directory(dirs, dirname, names):
    input_path, output_path = dirs

    for name in names:
        filename, ext = os.path.splitext(name)

        if ext in extensions_to_scrub:
            output_subdir = os.path.relpath(dirname, input_path)
            input_file = file(os.path.join(dirname, name))
            output_file = file(os.path.join(output_path, output_subdir, name), 'wt')

            print "Scrubbing file: %s..." % (os.path.join(output_subdir, name),)
            scrub_file(input_file, output_file)

            input_file.close()
            output_file.close()
    
def scrub_file_or_directory(path):
    real_path = os.path.abspath(path)

    if os.path.isfile(real_path):
        print "Scrubbing file... %s" % (real_path,)

        base_path, file_to_scrub = os.path.split(real_path)
        filename, ext = os.path.splitext(file_to_scrub)

        input_file = file(file_to_scrub)
        output_file = file(os.path.join(base_path, filename + '_scrubbed' + ext), 'wt')
        scrub_file(input_file, output_file)

        input_file.close()
        output_file.close()

    elif os.path.isdir(real_path):
        print "Scrubbing directory... %s" % (real_path,)
        scrubbed_dirname = os.path.basename(real_path) + '_scrubbed'
        output_path, whatever = os.path.split(real_path)  # This is weird, relpath doesn't work when built with py2exe

        scrubbed_path = os.path.join(output_path, scrubbed_dirname)
        base_output_dir = os.path.abspath(scrubbed_path)
        scrubbed_output_dir = base_output_dir

        count = 2
        while (os.path.isdir(scrubbed_output_dir)):
            scrubbed_output_dir = "%s%d" % (base_output_dir, count)
            count += 1

        print "Copying files to new directory at %s" % scrubbed_output_dir
        shutil.copytree(real_path, scrubbed_output_dir)
        os.path.walk(real_path, scrub_directory, (real_path, scrubbed_output_dir))

def usage(progname):
    print """Usage: %s <file_to_scrub> or
%s <directory_to_scrub>""" % (progname, progname)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scrub_file_or_directory(sys.argv[1])
        print "\n\nScrubbing all done!\n\nPress enter to close..."
        raw_input()
    else:
        usage(sys.argv[0])
