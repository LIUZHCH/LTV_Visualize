from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import GoogleCredentials
__author__ = 'z.liu'
# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

# [START all]
class bq_interface():
    #Initlize the bigquery library.
    def __init__(self,project_id):
        # [START build_service]
        #  Grab the application's default credentials from the environment.
        self.credentials = GoogleCredentials.get_application_default()
        # Construct the service object for interacting with the BigQuery API.
        self.bigquery_service = build('bigquery', 'v2', credentials=self.credentials)
        self.project_id = project_id;
        self.sql_all_userdata = "SELECT customer_id, SUM(total) as total, SUM(discount) as Discount, SUM(tax) as Tax\
                                FROM nipcola.order_mst_all \
                                GROUP BY customer_id \
                                ORDER BY total "
        self.sql_userdata_number =" select count(distinct customer_id) FROM nipcola.order_mst_all"
    # Execute the sql searching
    # sql_str : Sql string

    def __num_check(self,num):
        try:
            x = int(num)
            return True
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
            return False
    def __query(self, sql_str):
        try:
            query_request = self.bigquery_service.jobs()
            query_data = {
                'query': (
                sql_str)
            }
            return query_request.query(
                projectId=self.project_id,
                body=query_data).execute()
        except HttpError as err:
            print('Error: {}'.format(err.content))
            raise err
    def custom_query(self,sql_str):
        self.__query(sql_str)

    def get_userdate(self,start,end):
        limit_str = " Limit " + str(start) + ',' + str(end)
        return self.__query(self.sql_all_userdata + limit_str)

    def get_alluserdate(self,num = -1):
        if num == -1:
            limit_str = ""
        elif type(num) is str and self.__num_check():
            limit_str =" Limit " + num
        elif type(num) is int:
            limit_str =" Limit " + str(num)
        else:
            raise "Please input the number"
        return self.__query(self.sql_all_userdata + limit_str)

    def set_projectid(self,projectid):
        self.project_id = projectid;

    def getcustomer_num(self):
        data = self.__query(self.sql_userdata_number)
        return int(data['rows'][0]["f"][0]["v"])


def main(project_id):
    _bq_interface = bq_interface(project_id)
if __name__ == '__main__':
    #parser = argparse.ArgumentParser(
    #    description=__doc__,
    #    formatter_class=argparse.RawDescriptionHelpFormatter)
    #parser.add_argument('project_id', help='Your Google Cloud Project ID.')

   # args = parser.parse_args()

    main("pialab-rdmp")