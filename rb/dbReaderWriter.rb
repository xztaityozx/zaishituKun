# frozen_string_literal: true

require 'rubygems'
require 'sqlite3'

class ReaderWriter
  @dbname = './testdb.sqlite3'
  def self.getNameAndConditions(_id)
    response = [[]]
    SQLite3::Database.new @dbname do |db|
      response = db.execute('select * from members where id=?', _id)
    end
    response
  end

  def self.getTimecard(_id)
    response = [[]]
    SQLite3::Database.new @dbname do |db|
      response = db.execute('select * from timecard where id=?', _id)
    end
    response
  end
end

res = ReaderWriter.getTimecard '123456789abcde'
p res
