from airflow.models import DagBag


def test_dag_loading():
    dagbag = DagBag()
    dag = dagbag.get_dag(dag_id='dummy_dag')
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 1
