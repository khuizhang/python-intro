import tarfile
import os


def extractLJ(tarball):
    """ extract the lumberjack to /tmp dir """
    output_dir = "/tmp"
    gridTar = tarfile.open(tarball)
    gridTar.extractall(output_dir)
    for tarinfo in gridTar:
        if os.path.splitext(tarinfo.name)[-1] == ".gz":
            nodeTar = tarfile.open("/tmp/" + tarinfo.name)
            nodeTar.extractall(output_dir)
            nodeTar.close()
            os.remove("/tmp/" + tarinfo.name)
        else:
            os.remove("/tmp/" + tarinfo.name)
    gridTar.close()
