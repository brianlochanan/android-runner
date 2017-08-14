import os.path as op
import time
from util import makedirs
from Profiler import Profiler
import paths


class Volta(Profiler):
    def __init__(self, config):
        super(Volta, self).__init__(config)

    def start_profiling(self, device):
        super(Volta, self).start_profiling(device)
        device.shell('dumpsys batterystats --reset')
        device.unplug()  # reset plugs the device back in

    def stop_profiling(self, device):
        super(Volta, self).stop_profiling(device)

    def collect_results(self, device, path=None):
        super(Volta, self).collect_results(device)
        output_dir = op.join(paths.OUTPUT_DIR, 'volta/')
        makedirs(output_dir)
        with open(op.join(output_dir, '%s_%s.txt' % (device.id, time.strftime('%Y.%m.%d_%H%M%S'))), 'w+') as f:
            f.write(device.shell('dumpsys batterystats'))
