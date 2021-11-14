from modeller import *
from modeller.automodel import *    # Load the automodel class

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env,
              # file with template codes and target sequence
              alnfile  = 'alignment',
              # PDB codes of the templates
              knowns   = ('6baa'),
              # code of the target
              sequence = 'hKatp')
a.auto_align()                      # get an automatic alignment
a.make()                            # do homology modeling
~                                                           
