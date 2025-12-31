
from datetime import date
from project_handler import PROJECT_HANDLER
from random import shuffle


class Weekly():

    def __init__(self):
        self.project_handler = PROJECT_HANDLER()

    
    def create_week_id(self):
        today = date.today()
        year, week, _ = today.isocalendar()
        week_id = (year * 100) + week
        return week_id

    def check_week_init(self, new_week_id):
        old_week_id = self.project_handler.state.get("week_id")
        if old_week_id is None:
            self.project_handler.state["week_id"] = new_week_id

    def compare_week_id(self, new_week_id):
        old_week_id = self.project_handler.state.get("week_id")
        if new_week_id > old_week_id:
            return True
        return False
 
    def update_week_id(self, new_week_id):
        self.project_handler.state["week_id"] = new_week_id

    def is_weekly_done(self):
        done = self.project_handler.state.get("completed")
        return done

    def reset_weekly(self):
        self.project_handler.state["completed"] = False
    
    def add_score(self):
        self.project_handler.state["score"] += 1
    
    def remove_score(self):
        self.project_handler.state["score"] -= 2

    def shuffle_rotation(self):
        rotation = self.project_handler.state.get("rotation")
        done_topics = self.project_handler.state.get("done_topics")
        rotation.extend(done_topics)
        done_topics.clear()
        shuffle(rotation)
        
    def cycle_topic(self):
        rotation = self.project_handler.state.get("rotation")
        done_topics = self.project_handler.state.get("done_topics")
        current_topic = self.project_handler.state.get("topic")
 
        if rotation:
            next_topic = rotation.pop()
            done_topics.append(next_topic)
            self.project_handler.state["topic"] = next_topic
            return

        if not rotation:
            self.shuffle_rotation()
            if rotation:
                next_topic = rotation.pop()
                done_topics.append(next_topic)
                self.project_handler.state["topic"] = next_topic
                return
        
        self.project_handler.state["topic"] = "No topics loaded, use 'add topic:topic:topic' to add topics!"
    
    def init_topic_check(self):
        done_topics = self.project_handler.state.get("done_topics")
        current_topic = self.project_handler.state.get("topic")
        if done_topics and current_topic == "No topics loaded, use 'add topic:topic:topic' to add topics!":
            self.cycle_topic()

    def reset_all(self):
        self.project_handler.reset()
        print("reset")

    def reset_streak(self):
        self.project_handler.init()
        self.project_handler.state["streak"] = 0
        print("streak reset")
        self.visual()
        self.project_handler.save_project()

    def reset_score(self):
        self.project_handler.init()
        self.init_topic_check()
        new_week_id = self.create_week_id()
        check_week_init = self.check_week_init(new_week_id)
        self.project_handler.state["score"] = 0
        self.visual()        
        self.project_handler.save_project()

    def list_topics(self):
        self.project_handler.init()
        self.init_topic_check()
        new_week_id = self.create_week_id()
        check_week_init = self.check_week_init(new_week_id)
        rotation = self.project_handler.state.get("rotation")
        done_topics = self.project_handler.state.get("done_topics")
        
        all_topics = list()
        all_topics.extend(rotation)
        all_topics.extend(done_topics)
        self.visual()
        print("Topics:")
        for topic in all_topics:
            print(topic)

    def add_topics(self, topic_string):
        self.project_handler.init()

        new_week_id = self.create_week_id()
        check_week_init = self.check_week_init(new_week_id)
        topics = topic_string.split(":") 
        done_topics = self.project_handler.state.get("done_topics")
        for topic in topics:
            if topic == "":
                continue
            topic = topic.strip()
            done_topics.append(topic)
        
        self.init_topic_check()
        self.visual()
        self.project_handler.save_project()

    def topic_done(self):
        self.project_handler.init()
        self.init_topic_check()
        new_week_id = self.create_week_id()
        check_week_init = self.check_week_init(new_week_id)
        self.project_handler.state["completed"] = True
        self.add_score()
        self.cycle_topic()
        
        self.visual()
        self.project_handler.save_project()

    def skip_topic(self):
        self.project_handler.init()
        self.init_topic_check()
        
        # We don't change the score or the completed status
        # We just move to the next topic
        self.cycle_topic()
        
        print("Topic skipped.")
        self.visual()
        self.project_handler.save_project()

    def update(self):
            self.project_handler.init()
            
            weekly_done = self.is_weekly_done()
            
            new_week_id = self.create_week_id()
            self.check_week_init(new_week_id)
            compare_week_id = self.compare_week_id(new_week_id)
            self.init_topic_check()
            
            if compare_week_id:
                self.update_week_id(new_week_id)
                # If week changed and previous week was finished, increment streak
                if weekly_done:
                    current_streak = self.project_handler.state.get("streak", 0)
                    self.project_handler.state["streak"] = current_streak + 1
                    self.reset_weekly()
                else:
                    # If week changed and previous week NOT finished, lose streak and points
                    self.project_handler.state["streak"] = 0
                    self.remove_score()
                
                self.cycle_topic()

            self.project_handler.save_project()
         

    def show(self):
        self.update()
        self.visual()
    

    def streak_flame_multiplier(self):
        streak = self.project_handler.state.get("streak", 0)
        flames_count = (streak // 4) + 1
        final_count = min(flames_count, 6)
        return "🔥" * final_count


    def visual(self):
        week_id = self.project_handler.state.get("week_id")
        score = self.project_handler.state.get("score")
        streak = self.project_handler.state.get("streak", 0)
        weekly_done = self.project_handler.state.get("completed")
        topic = self.project_handler.state.get("topic")

        week_id_str = str(week_id)
        year = week_id_str[:4]
        week = week_id_str[4:]
    
        streak_flames = self.streak_flame_multiplier()
        status = "Weekly completed hurray!" if weekly_done else "Weekly not completed :("
        
        print(f"\n---- WEEK {week} / {year} ----")
        print(f"Score  : {score}")
        print(f"Streak : {streak} {streak_flames}")
        print(f"Status : {status}")
        print(f"Topic  : {topic}")
        print("------------------------")  
                
