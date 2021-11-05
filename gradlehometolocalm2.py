import sys
import os
# import subprocess
import glob
# import shutil

def main(argv):
  # project_dir = os.path.dirname(os.path.realpath(__file__))
  repo_dir = os.path.join("/Users/wengjiadong", "m2localrepo")
  temp_home = os.path.join("/Users/wengjiadong", ".gradle")

  print "[The repository modules in %s will be moved to %s]" % (temp_home, repo_dir)

  # if not os.path.isdar(temp_home):
  #   os.makedirs(temp_home)

  # if os.path.isdir(repo_dir):
  #   shutil.rmtree(repo_dir)

  # subprocess.call(["gradle", "-g", temp_home, "-Dbuild.network_access=allow"])

  # mapping for the target files
  # .gradle/caches/modules-2/files-2.1
  # |- javax.servlet
  # |   |- javax.servlet-api
  # |      |- 3.1.0
  # |         |- 330afdf2f976af1584c6a18333f4d53d264df1de
  # |         |   |--- javax.servlet-api-3.1.0.pom
  # |         |- 3cd63d075497751784b2fa84be59432f4905bf7c
  # |         |   |--- javax.servlet-api-3.1.0.jar
  # |         |- ab3976d4574c48d22dc1abf6a9e8bd0fdf928223
  # |             |--- javax.servlet-api-3.1.0-sources.jar
  # |- net.java
  #     |- jvnet-parent
  #        |- 3
  #           |- f8f3be3e980551a39b5679411e171aeb6931aaec
  #               |--- jvnet-parent-3.pom
  cache_files = os.path.join(temp_home, "caches/modules-*/files-*")
  # loop in targets (e.g. ~/.gradle/caches/modules-2/files-2.1)
  for cache_dir in glob.glob(cache_files):
    # list target directories
    for cache_group_id in os.listdir(cache_dir):
      cache_group_dir = os.path.join(cache_dir, cache_group_id)
      repo_group_dir = os.path.join(repo_dir, cache_group_id.replace('.', '/'))
      for cache_artifact_id in os.listdir(cache_group_dir):
        cache_artifact_dir = os.path.join(cache_group_dir, cache_artifact_id)
        repo_artifact_dir = os.path.join(repo_group_dir, cache_artifact_id)
        for cache_version_id in os.listdir(cache_artifact_dir):
          cache_version_dir = os.path.join(cache_artifact_dir, cache_version_id)
          repo_version_dir = os.path.join(repo_artifact_dir, cache_version_id)
          if not os.path.isdir(repo_version_dir):
            os.makedirs(repo_version_dir)
          cache_items = os.path.join(cache_version_dir, "*/*")
          for cache_item in glob.glob(cache_items):
            cache_item_name = os.path.basename(cache_item)
            repo_item_path = os.path.join(repo_version_dir, cache_item_name)
            print "%s:%s:%s (%s)" % (cache_group_id, cache_artifact_id, cache_version_id, cache_item_name)
            # shutil.copyfile(cache_item, repo_item_path)
  # shutil.rmtree(temp_home)
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))
