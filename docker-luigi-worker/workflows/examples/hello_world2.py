import luigi
import datetime

class HelloWorldTask(luigi.Task):
    task_namespace = 'examples'
    
    date = luigi.DateParameter(default=datetime.date.today())
    def run(self):
        print("{task} says: Hello world! at date: {date} ".format(task=self.__class__.__name__,date=date))


class AllReports(luigi.WrapperTask):
    date = luigi.DateParameter(default=datetime.date.today())
    def requires(self):
        yield HelloWorldTask(self.date)

#if __name__ == '__main__':
#    luigi.run(['examples.HelloWorldTask', '--workers', '1'])
