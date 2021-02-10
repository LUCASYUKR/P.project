package mrc_ex;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;



public class WordCount { //driver class
	
	public static void main(String[] args) throws Exception{
		
		Configuration conf = new Configuration(); //hadoop ȯ�漳�� ����
		
		if(args.length!=2) { //���� ���ڿ��� 2���� �ƴϸ� ���α׷� ���� = args[0]=key(text),args[1]=value(wordcount) 2�� ���ڿ�
			System.err.println("Usage : WordCount <input><output>");
			System.exit(2);
		}
		
		Job job = new Job(conf,"WordCount"); //hadoop �۾�ȯ�� ����
		
		job.setJarByClass(WordCount.class);
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0])); //�о�� ���ϸ� 
		FileOutputFormat.setOutputPath(job, new Path(args[1])); //���� ���� ���ϸ�
		
		job.waitForCompletion(true);
	}

}
