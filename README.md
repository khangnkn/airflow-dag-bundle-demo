# airflow-dag-bundle-demo

Public demo repository for an Airflow `GitDagBundle`.

The DAG file is `dags/hello_git_bundle.py`. Point the bundle at this repo with:

```yaml
dagProcessor:
  dagBundleConfigList:
    - name: example-git
      classpath: airflow.providers.git.bundles.git.GitDagBundle
      kwargs:
        repo_url: https://github.com/khangnkn/airflow-dag-bundle-demo.git
        tracking_ref: main
        subdir: dags
        refresh_interval: 30
```

No token belongs in `repo_url`. This repository is public. A private repository should use `git_conn_id` instead.
