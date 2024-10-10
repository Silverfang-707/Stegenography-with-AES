require 'fiber'

conversation = [
  { sender: 'Faculty', message: 'Hello Students' },
  { sender: 'Student', message: 'Hello Sir' },
  { sender: 'Faculty', message: 'What is your Register number' },
  { sender: 'Student', message: '22MIS1088' },
  { sender: 'Faculty', message: 'All the best' },
  { sender: 'Student', message: 'Thankyou Sir' },
]

def start_conversation(participant, messages)
  fiber = Fiber.new do
    messages.each do |msg|
      if msg[:sender] == participant
        puts "#{participant}: #{msg[:message]}"
        Fiber.yield
      end
    end
  end

  while fiber.alive?
    fiber.resume
    sleep(1)
  end
end

thread_1 = Thread.new do
  start_conversation('Faculty', conversation)
end

thread_2 = Thread.new do
  start_conversation('Student', conversation)
end

thread_1.join
thread_2.join
