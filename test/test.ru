require 'fileutils'

class ContentManagementSystem
  CONTENT_DIR = 'Desktop'

  def initialize
    FileUtils.mkdir_p(CONTENT_DIR)
  end

  def menu
    loop do
      puts "\nContent Management System"
      puts "1. List content"
      puts "2. Add content"
      puts "3. Edit content"
      puts "4. Delete content"
      puts "5. View content"
      puts "6. Exit"
      print "Choose an option: "
      choice = gets.chomp.to_i

      case choice
      when 1
        list_content
      when 2
        add_content
      when 3
        edit_content
      when 4
        delete_content
      when 5
        view_content
      when 6
        break
      else
        puts "Invalid option. Please try again."
      end
    end
  end

  def list_content
    puts "\nListing all content titles:"
    Dir.entries(CONTENT_DIR)
       .select { |f| !File.directory? f }
       .each { |file| puts File.basename(file, ".txt") }
  end

  def add_content
    print "\nEnter title: "
    title = gets.chomp
    print "Enter content: "
    content = gets.chomp
    File.write(File.join(CONTENT_DIR, "#{title}.txt"), content)
    puts "Content added successfully."
  end

  def edit_content
    print "\nEnter title of the content to edit: "
    title = gets.chomp
    file_path = File.join(CONTENT_DIR, "#{title}.txt")
    
    if File.exist?(file_path)
      print "Enter new content: "
      content = gets.chomp
      File.write(file_path, content)
      puts "Content edited successfully."
    else
      puts "Content not found."
    end
  end

  def delete_content
    print "\nEnter title of the content to delete: "
    title = gets.chomp
    file_path = File.join(CONTENT_DIR, "#{title}.txt")
    
    if File.exist?(file_path)
      FileUtils.rm(file_path)
      puts "Content deleted successfully."
    else
      puts "Content not found."
    end
  end

  def view_content
    print "\nEnter title of the content to view: "
    title = gets.chomp
    file_path = File.join(CONTENT_DIR, "#{title}.txt")
    
    if File.exist?(file_path)
      puts "\nContent of #{title}:"
      puts File.read(file_path)
    else
      puts "Content not found."
    end
  end
end

cms = ContentManagementSystem.new
cms.menu
