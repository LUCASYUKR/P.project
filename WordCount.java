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



public class WordCount { 
	
	public static void main(String[] args) throws Exception{
		
		Configuration conf = new Configuration();
		
		if(args.length!=2) { //들어온 문자열이 2개가 아니면 프로그램 종료 = args[0]=key(text),args[1]=value(wordcount) 2개 문자열
			System.err.println("Usage : WordCount <input><output>");
			System.exit(2);
		}
		
		Job job = new Job(conf,"WordCount"); //hadoop 작업환경 설정
		
		job.setJarByClass(WordCount.class);
		job.setMapperClass(WordCountMapper.class);
		job.setReducerClass(WordCountReducer.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0])); //읽어올 파일명 
		FileOutputFormat.setOutputPath(job, new Path(args[1])); //새로 만들어낼 파일명
		
		job.waitForCompletion(true);
	}

}
