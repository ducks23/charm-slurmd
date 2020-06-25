import logging, sys

sys.path.append('lib')

from ops.charm import CharmBase

from ops.main import main

from slurm_snap_manager import SlurmSnapInstanceManager

class SlurmdCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)
        self.slurm_snap = SlurmSnaInstanceManager(self, "slurmd")
        self.framework.observe(self.on.install, self.on_install)

    def on_install(self, event):
        self.slurm_snap.install()

if __name__ == "__main__":
    main(SlurmdCharm)
