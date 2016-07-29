# Run create_clusters.py! has to be modified for PRWP and MAA
./exp_score_cluster.py PRWP
./txt_score_cluster.py PRWP
./know_score_cluster.py PRWP

./exp_score_cluster.py MAA
./txt_score_cluster.py MAA
./know_score_cluster.py MAA

./exp_score_cluster.py PRWP CANCER
./txt_score_cluster.py PRWP CANCER
./know_score_cluster.py PRWP CANCER

./exp_score_cluster.py MAA CANCER
./txt_score_cluster.py MAA CANCER
./know_score_cluster.py MAA CANCER
