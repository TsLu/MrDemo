HADOOP="/home/work/local/hadoop/bin/hadoop"

DATE=`date -d 1" days ago" +%Y%m%d`
HDPATH_input="/app/test/minos/200047343/textlog/70016628/$DATE/*/*"
HDPATH_input2="/log/200047343/test_case/$DATE/*/*"
PYTHON="/home/work/tools/usr/bin/python"

function map_reduce()
{
    $HADOOP dfs -rmr $OUTPUT
    $HADOOP streaming \
        -D stream.num.map.output.key.fields=1 \
    	-D num.key.fields.for.partition=3 \
    	-D mapreduce.map.output.compress=true \
    	-inputformat org.apache.hadoop.mapred.CombineTextInputFormat \
        -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
        -cacheArchive '/app/tools/test/python.tar.gz#python' \
        -input $INPUT1 \
        -input $INPUT2 \
        -output $OUTPUT \
	    -mapper "python/bin/python mapper.py" \
        -reducer "python/bin/python reducer.py" \
	    -file mapper.py reducer.py \
	    -jobconf stream.memory.limit=4096 \
	    -jobconf mapred.max.split.size=5368709120 \
        -jobconf mapred.job.priority=HIGH \
        -jobconf mapred.map.tasks=100 \
        -jobconf mapred.reduce.tasks=10 \
        -jobconf mapred.job.name="test_case"
    return $?
}

INPUT1=$HDPATH_input/*
INPUT2=$HDPATH_input2/*
OUTPUT=/app/test/cases/test_case/savelog_test/$DATE

map_reduce